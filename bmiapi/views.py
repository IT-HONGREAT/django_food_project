from rest_framework.views import APIView
import joblib
import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView


class BmiPrediction(APIView):
    def post(self, request):
        # input data change to dataframe for prediction
        def info_to_df(height, weight, gender):
            height, weight = height / 100, weight / 100
            check = pd.DataFrame(columns=["Height", "Weight", "gender"])
            data_to_insert = {"Height": height, "Weight": weight, "gender": gender}
            infodf = check.append(data_to_insert, ignore_index=True)
            return infodf

        """
        json input example; height, weight, sex(gender 0:female, 1:male)
        {
            "height":170,
            "weight":70,
            "sex":1
        }
        """
        data = request.data

        height = data["height"]
        weight = data["weight"]
        sex = data["sex"]

        # 입력값 적용
        loaded_model = joblib.load("bmi/ml_model/bmi_model.pkl")
        prediction = loaded_model.predict(info_to_df(height, weight, sex))

        prediction_dict = {1: "깡마름", 2: "마름", 3: "보통", 4: "통통", 5: "뚱뚱"}

        prediction_name = prediction_dict[prediction[0]]

        # json output { "prediction_name": prediction_name }
        return Response({"prediction_name": prediction_name}, status=200)
