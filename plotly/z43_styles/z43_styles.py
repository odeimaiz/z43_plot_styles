import plotly.graph_objs as go
import plotly.io as pio

pio.templates["z43_base"] = go.layout.Template(
    layout=dict(
        font=dict(
            size=14,
            family="Roboto"
        ),
        title=dict(
            x=0.5,
            font=dict(
                size=22,
                family="Roboto"
            ),
        ),
        xaxis=dict(
            title=dict(
                font=dict(
                    size=16,
                    family="Roboto"
                )
            ),
            ticks="outside"
        ),
        yaxis=dict(
            title=dict(
                font=dict(
                    size=16,
                    family="Roboto"
                )
            ),
            ticks="outside"
        ),
    )
)

pio.templates["z43_dark"] = go.layout.Template(
    layout=dict(
        font=dict(
            color="#FFFFFF"
        ),
        plot_bgcolor="#202020",
        paper_bgcolor="#202020",
        xaxis=dict(
            title=dict(
                font=dict(
                    color="#BFBFBF"
                )
            ),
            tickfont=dict(
                color="#BFBFBF"
            ),
            tickcolor="#BFBFBF",
            gridcolor="#373737",
            linecolor="#373737",
            zerolinecolor="#373737"
        ),
        yaxis=dict(
            title=dict(
                font=dict(
                    color="#BFBFBF"
                )
            ),
            tickfont=dict(
                color="#BFBFBF"
            ),
            tickcolor="#BFBFBF",
            gridcolor="#373737",
            linecolor="#373737",
            zerolinecolor="#373737"
        )
    )
)
