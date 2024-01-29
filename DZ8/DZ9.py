import pandas as pd
from sklearn.preprocessing import LabelBinarizer

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot encoding
label_binarizer = LabelBinarizer()
one_hot_encoded = label_binarizer.fit_transform(data['whoAmI'])

# Создание DataFrame из one-hot encoding
one_hot_df = pd.DataFrame(one_hot_encoded, columns=label_binarizer.classes_)

# Объединение исходного DataFrame и нового DataFrame с one-hot encoding
data = pd.concat([data, one_hot_df], axis=1)

# Удаление исходного столбца 'whoAmI'
data = data.drop('whoAmI', axis=1)

# Вывод результата
data.head()