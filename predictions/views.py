from django.shortcuts import render

import joblib
import os
import pandas as pd
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChurnInputSerializer

class PredictChurnView(APIView):
    # Cargar una sola vez para eficiencia
    MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictions/ml_models/modelo_churn_telmex.pkl')
    SCALER_PATH = os.path.join(settings.BASE_DIR, 'predictions/ml_models/escalador_churn.pkl')
    
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    def post(self, request):
        serializer = ChurnInputSerializer(data=request.data)
        if serializer.is_valid():
            df_input = pd.DataFrame([serializer.validated_data])
            # Aplicar el escalador que guardamos
            data_scaled = self.scaler.transform(df_input)
            prediction = self.model.predict(data_scaled)[0]
            prob = self.model.predict_proba(data_scaled)[0][1]
            
            return Response({
                'churn': int(prediction),
                'probability': round(prob * 100, 2)
            })
        return Response(serializer.errors, status=400)