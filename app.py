# -*- coding: utf-8 -*-
import os
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

DEBUG = True

app = dash.Dash(__name__)
server = app.server  # the Flask app

app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True

# Static Path to images
STATIC_PATH = os.path.join(os.getcwd(), 'images/')

# Main App
app.layout = html.Div([
    # Banner display
    html.Div([
        html.H2(
            'Task-oriented Function Detection',
            id='title',
        ),
        html.Img(
            src="https://wwwdc05.adst.keio.ac.jp/kj/vi/common/img/thumbF2.png",
            style={
                'height': '60px',
                'margin-top': '8px',
                'margin-bottom': '0px'
            }
        )
    ],
        className="banner",
        style={
        'background-color': '#1A8695',
        'height': '75px',
        'padding-top': '0px',
        'padding-left': '0px',
        'padding-right': '0px',
        'width': '100%',
        'margin-bottom': '10px',
    }
    ),

    # Body
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    'original image',
                ],
                    style={
                    'color': 'rgb(0,0,0)',
                    'font-size': 'x-large',
                    'position': 'relative',
                    'margin-top': '8px',
                    'left': '200px'
                }),
                html.Img(
                    style={
                        'width': '70%',
                        'height': 'auto',
                        'margin': '10px 30px 0px 30px'
                    },
                    id="input_image",
                    alt="サンプル",
                )
            ],
                style={
                'color': 'rgb(255,255,255)',
                'float': 'left',
                'margin-bottom': '0px',
                'margin-right': '-200px'
            }
            ),

            html.Div([
                html.Div([
                    'task-oriented function',
                ],
                    style={
                    'color': 'rgb(0,0,0)',
                    'font-size': 'x-large',
                    'margin-top': '8px',
                    'position': 'relative',
                    'left': '150px'
                }),
                html.Img(
                    style={
                        'width': '70%',
                        'height': 'auto',
                        'margin': '10px 30px 0px 30px'
                    },
                    id="output_image",
                ),
            ],
                style={
                'color': 'rgb(255,255,255)',
                'float': 'left',
                'margin-bottom': '0px',
                'margin-right': '-150px'
            }
            ),

            html.Div([
                html.Img(
                    src=STATIC_PATH + 'label.png',
                    style={
                        'width': '50%',
                        'height': 'auto',
                    },
                ),
            ],
                style={
                'float': 'left',
                'margin-bottom': '0px',
                'margin-top': '150px',
            }
            ),

            html.Div([

                html.Div([
                    "Select an object",
                    dcc.Dropdown(
                        options=[
                            {
                                'label': 'hammer0',
                                'value': 'hammer0'
                            },
                            {
                                'label': 'hammer1',
                                'value': 'hammer1'
                            },
                            {
                                'label': 'hammer2',
                                'value': 'hammer2'
                            },
                            {
                                'label': 'ladle0',
                                'value': 'ladle0'
                            },
                            {
                                'label': 'ladle1',
                                'value': 'ladle1'
                            },
                            {
                                'label': 'ladle2',
                                'value': 'ladle2'
                            },
                            {
                                'label': 'scissors0',
                                'value': 'scissors0'
                            },
                            {
                                'label': 'scissors1',
                                'value': 'scissors1'
                            },
                            {
                                'label': 'scissors2',
                                'value': 'scissors2'
                            }
                        ],
                        value='hammer0',
                        id='image_selection',
                        clearable=False
                    )
                ],
                    style={
                    'margin': '10px 50px',
                    'float': 'left',
                    'font-size': 'large',
                    'width': '25%'
                }
                ),



                html.Div([
                    "Select a task",
                    dcc.RadioItems(
                        options=[
                            {'label': ' Grasp　', 'value': '0'},
                            {'label': ' Hand　', 'value': '1'},
                            {'label': ' Hit　', 'value': '2'},
                            {'label': ' Scoop　', 'value': '3'},
                            {'label': ' Cut　', 'value': '4'},
                        ],
                        value='0',
                        id='task_selection',
                        labelStyle={'display': 'inline-block'}
                    )
                ],
                    style={
                    'margin': '10px 100px',
                    'float': 'left',
                    'font-size': 'large'
                }
                ),
            ],
                style={
                'margin': '30px 10px',
                'clear': 'both',
                'font-size': 'large',
                'width': '100%'
            }
            )


        ],
            className="row"
        ),
    ],
        style={
        'width': '100%',
        'margin': '10px 50px',
    },
        className="container scalable"
    )
])


# load an original image
@app.callback(
    Output("input_image", "src"),
    [Input("image_selection", "value")])
def update_original_image(image):
    out = STATIC_PATH + image + '.jpg'
    return out


@app.callback(
    Output("output_image", "src"),
    [Input("task_selection", "value")],
    [State("image_selection", "value")])
def update_result_image(task, image):
    out = STATIC_PATH + image + '_' + task + '.jpg'
    return out


@app.server.route('{}<path:image_path>'.format(STATIC_PATH))
def serve_image(image_path):
    return flask.send_file(STATIC_PATH + image_path)


external_css = [
    # Normalize the CSS
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
    "https://fonts.googleapis.com/css?family=Open+Sans|Roboto"  # Fonts
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://cdn.rawgit.com/xhlulu/9a6e89f418ee40d02b637a429a876aa9/raw/base-styles.css",
    "https://cdn.rawgit.com/plotly/dash-object-detection/875fdd6b/custom-styles.css"
]

for css in external_css:
    app.css.append_css({"external_url": css})


if __name__ == '__main__':
    app.run_server(debug=DEBUG)
