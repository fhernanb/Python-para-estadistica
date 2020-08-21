import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer, ColumnTransformer
from sklearn.model_selection import train_test_split

df = pd.read_csv('train.csv')
df.head()

df = df.dropna(subset=['Pclass', 'Sex', 'Age', 'Embarked', 'Fare', 'SibSp'])

X = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
y = df.Survived.values

preprocesador = make_column_transformer(
    (['Age', 'Fare'], StandardScaler()),
    (['Sex', 'Pclass', 'Embarked'], OneHotEncoder())
)

X = preprocesador.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
model = Sequential()
model.add(Dense(32, input_shape=(X_train.shape[1],), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adadelta', metrics=['acc'])

model.fit(X_train, y_train, epochs=100, batch_size=64)

def predict(Pclass=1, Sex='female', Age=60 ,Fare=0, Embarked='C'):
  cnames = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
  data = [[Pclass, Sex, Age, Fare, Embarked]]
  my_X = pd.DataFrame(data=data, columns=cnames)
  my_X = preprocesador.transform(my_X)
  return model.predict_classes(my_X)

  predict()
