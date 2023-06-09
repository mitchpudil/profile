import dash_html_components as html

perception_video = [
            html.Iframe(
                src="https://www.youtube.com/embed/Yj0VRObArv8",
                width="560",
                height="315",
                title="YouTube video player",
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            )]


LAYOUT = html.Div(
    perception_video
)


