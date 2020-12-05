import tarfile

from chinese_SA.dataLoader import DataLoader
from chinese_SA.model import Model

models = {
    ('bert', "bert-base-chinese"): None,
}


def unpack_model(model_name):
    tar = tarfile.open(f"{model_name}.tar.gz", "r:gz")
    tar.extractall()
    tar.close()


data = DataLoader()
for model_tuple in models:
    model = Model(*model_tuple)
    model.train_model(data.get_train_df(), data.num_labels)
    models[model_tuple] = model

for model in models.values():
    accuracy = model.eval_model(data.get_test_df())
    print(accuracy)
