"""Code to extract a color palette from a PIL Image."""

import colorspacious
import numpy as np
import pandas as pd
from PIL import Image
from sitemotive.colors.color import ColorConverter
from sklearn.cluster import KMeans

def resize_image(image, max_img_size):
    """Resizes an image while preserving its aspect ratio.

    Parameters
    ----------
    image : str
        local location of image

    max_img_size : int
        Maximum size of image to use in processing

    Returns
    -------
    PIL.Image
        Resized image
    """
    # Resize the image to fit within max_img_size while preserving its aspect ratio
    if max(image.size[0], image.size[1]) > max_img_size:
        if image.size[0] > image.size[1]:
            wpercent = (max_img_size / float(image.size[0]))
            hsize = int((float(image.size[1]) * float(wpercent)))
            image = image.resize((max_img_size, hsize), Image.ANTIALIAS)
        else:
            hpercent = (max_img_size / float(image.size[1]))
            wsize = int((float(image.size[0]) * float(hpercent)))
            image = image.resize((wsize, max_img_size), Image.ANTIALIAS)

    return image


def image_to_cam_array(image):
    """Translate PIL image to a numpy array of CAM02UCS colors

    Parameters
    ----------
    image : PIL.Image
        PIL Image

    Returns
    -------
    np.array
        array of CAM02UCS color values
    """
    # Open the image using PIL
    image = image.convert('RGB')
    # Convert the image to CAM02UCS color space
    cam_image = colorspacious.cspace_convert(np.array(image), "sRGB255", "CAM02-UCS").reshape(-1,3)
    return cam_image


def get_clusters(pixel_array, n_clusters):
    """Perform clustering on pixel array using KMeans and return resulting cluster labels

    Parameters
    ----------
    pixel_array : np.array
        numpy array of pixels

    n_clusters : int
        number of clusters to use

    Returns
    -------
    np.array
        array of cluster labels
    np.array
        array of cluster centers
    """
    clustering = KMeans(n_clusters=n_clusters, random_state=42).fit(pixel_array)
    return clustering.labels_, clustering.cluster_centers_


def get_unique_colors(cluster_centers):
    """Remove similar colors from resulting clusters and return list of unique colors along with their minimum distances

    Parameters
    ----------
    cluster_centers : np.array
        array of cluster centers

    Returns
    -------
    list
        list of unique colors along with their minimum distances
    """
    unique_colors = []
    for i, center in enumerate(cluster_centers):
        distances = np.linalg.norm(center - cluster_centers, axis=1)
        distances[i] = np.inf
        min_dist = np.min(distances)
        if len(unique_colors) == 0  or not (min_dist in [c[1] for c in unique_colors] and min_dist < 10):
            unique_colors.append((i, min_dist))
    return unique_colors


def get_color_scores(cluster_centers, cluster_labels, min_dist_threshold=10):
    """Calculate the weighted score for each unique color based on dominance and distinctiveness.

    Parameters
    ----------
    cluster_centers : np.array
        Array of cluster centers for the image

    cluster_labels : np.array
        Array of labels for the pixels in the image

    min_dist_threshold : float, optional
        The minimum distance threshold to consider colors as distinct. Colors with distances
        below this threshold will be considered similar. Default is 10.

    Returns
    -------
    list
        List of tuples containing:
            - hexcode (str): One of the hexcodes that makes up the palette
            - dominance_score (float): Approximately how much that color makes up the image
            - min_dist (float): Minimum distance found between the color and other colors considered

    The function calculates a weighted score for each unique color in an image's palette.
    The score is based on two factors: dominance and color distinctiveness.

    The dominance score represents the approximate percentage of the image covered by a particular color.
    The color distinctiveness is determined by the minimum distance between a color and other colors considered in the palette.
    By combining these factors, the function generates a weighted score for each unique color.
    """
    unique_colors = []

    for i, center in enumerate(cluster_centers):
        center = np.array([round(c, 2) for c in center])
        distances = np.linalg.norm(center - cluster_centers, axis=1)
        distances[i] = np.inf
        min_dist = np.min(distances)
        if len(unique_colors) == 0 or not (min_dist in [c[1] for c in unique_colors] and min_dist < min_dist_threshold):
            pixels = np.where(cluster_labels == i)
            dominance_score = len(pixels[0]) / len(cluster_labels)
            rgb = ColorConverter.CAM02UCS_to_RGB(center)
            hexcode = ColorConverter.RGB_to_HEX(rgb)
            unique_colors.append((hexcode, dominance_score, min_dist))
    return unique_colors


def extract_colors(pil_image, max_img_size=150, n_clusters=10, max_colors=7, min_dist_cutoff=8):
    """Extract color palette from an image

    Parameters
    ----------
    image : str or PIL
        PIL Image

    max_img_size : int, optional
        Maximum size of image to use in processing, by default 150

    n_clusters : int, optional
        number of initial clusters to pass resized image through, by default 10

    max_colors : int, optional
        Maximum number of colors to use in resulting color palette, by default 7

    min_dist_cutoff : int, optional
        Minimum distance between other colors that a color needs to have in order to not be considered a
        duplicate color, by default 8

    Returns
    -------
    pd.DataFrame
        DataFrame of the resulting palette with columns for:
            - hexcode (str): One of the hexcodes that makes up the palette
            - dominance_score (float): Approximately how much that color makes up the image
            - min_dist (float): Minimum distance found between the color and other colors considered
    """
    # Get clusters
    image = resize_image(pil_image, max_img_size)
    pixel_array = image_to_cam_array(image)
    n_clusters = min(n_clusters, np.unique(pixel_array, axis=0).shape[0])
    cluster_labels, cluster_centers = get_clusters(pixel_array, n_clusters)

    # Get minimum distances
    scores = get_color_scores(cluster_centers, cluster_labels)

    # Sort the list of unique colors based on their weighted score
    scores.sort(key=lambda x: x[1], reverse=True)

    # Return the top N unique colors with the highest weighted scores and are not too similar to each other
    df = pd.DataFrame(scores, columns=['hexcode', 'dominance_score', 'min_dist'])

    if (df.loc[df['min_dist'] > min_dist_cutoff].shape[0]) > 3:
        return df.loc[(df['min_dist'] > min_dist_cutoff)].iloc[:max_colors,:]

    return df.reset_index(drop=True).iloc[:max_colors,:]
