import sklearn.datasets

from c3pml import C3PML

app = C3PML(
    model_reg=None,
)


def create_model():
    return sklearn.ensemble.RandomForestClassifier()


@app.train
def train():
    model = create_model()

    x_data, y_data = sklearn.datasets.load_boston(return_X_y=True)

    model.fit(x_data, y_data)
