{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MATHIDINESH/STOCK-MARKET/blob/main/market_prediction.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f53fcbbf-a62d-4aa2-be7b-9aa4e17a5e48",
      "metadata": {
        "id": "f53fcbbf-a62d-4aa2-be7b-9aa4e17a5e48"
      },
      "outputs": [],
      "source": [
        "import yfinance as yf\n",
        "import pandas as pd\n",
        "import os"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0c4d2b51-1187-44c7-a281-da84d0381dd5",
      "metadata": {
        "id": "0c4d2b51-1187-44c7-a281-da84d0381dd5"
      },
      "outputs": [],
      "source": [
        "if os.path.exists(\"sp500.csv\"):\n",
        "    sp500 = pd.read_csv(\"sp500.csv\", index_col=0)\n",
        "else:\n",
        "    sp500 = yf.Ticker(\"^GSPC\")\n",
        "    sp500 = sp500.history(period=\"max\")\n",
        "    sp500.to_csv(\"sp500.csv\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f605b43c-8db9-43ae-b2d4-29fc6048b8aa",
      "metadata": {
        "id": "f605b43c-8db9-43ae-b2d4-29fc6048b8aa"
      },
      "outputs": [],
      "source": [
        "sp500.index = pd.to_datetime(sp500.index)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fbb162ce-7d18-4c14-b349-9014c0d6db42",
      "metadata": {
        "id": "fbb162ce-7d18-4c14-b349-9014c0d6db42",
        "outputId": "4d4c9d70-b513-4448-8d44-729dad395799"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Open</th>\n",
              "      <th>High</th>\n",
              "      <th>Low</th>\n",
              "      <th>Close</th>\n",
              "      <th>Volume</th>\n",
              "      <th>Dividends</th>\n",
              "      <th>Stock Splits</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1950-01-03</th>\n",
              "      <td>16.660000</td>\n",
              "      <td>16.660000</td>\n",
              "      <td>16.660000</td>\n",
              "      <td>16.660000</td>\n",
              "      <td>1260000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1950-01-04</th>\n",
              "      <td>16.850000</td>\n",
              "      <td>16.850000</td>\n",
              "      <td>16.850000</td>\n",
              "      <td>16.850000</td>\n",
              "      <td>1890000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1950-01-05</th>\n",
              "      <td>16.930000</td>\n",
              "      <td>16.930000</td>\n",
              "      <td>16.930000</td>\n",
              "      <td>16.930000</td>\n",
              "      <td>2550000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1950-01-06</th>\n",
              "      <td>16.980000</td>\n",
              "      <td>16.980000</td>\n",
              "      <td>16.980000</td>\n",
              "      <td>16.980000</td>\n",
              "      <td>2010000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1950-01-09</th>\n",
              "      <td>17.080000</td>\n",
              "      <td>17.080000</td>\n",
              "      <td>17.080000</td>\n",
              "      <td>17.080000</td>\n",
              "      <td>2520000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-06</th>\n",
              "      <td>3930.889893</td>\n",
              "      <td>3942.550049</td>\n",
              "      <td>3886.750000</td>\n",
              "      <td>3908.189941</td>\n",
              "      <td>2209800080</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-07</th>\n",
              "      <td>3909.429932</td>\n",
              "      <td>3987.889893</td>\n",
              "      <td>3906.030029</td>\n",
              "      <td>3979.870117</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-08</th>\n",
              "      <td>3959.939941</td>\n",
              "      <td>4010.500000</td>\n",
              "      <td>3944.810059</td>\n",
              "      <td>4006.179932</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-09</th>\n",
              "      <td>4022.939941</td>\n",
              "      <td>4076.810059</td>\n",
              "      <td>4022.939941</td>\n",
              "      <td>4067.360107</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-12</th>\n",
              "      <td>4083.669922</td>\n",
              "      <td>4119.279785</td>\n",
              "      <td>4083.669922</td>\n",
              "      <td>4107.279785</td>\n",
              "      <td>1602969000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>18292 rows × 7 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                   Open         High          Low        Close      Volume  \\\n",
              "Date                                                                         \n",
              "1950-01-03    16.660000    16.660000    16.660000    16.660000     1260000   \n",
              "1950-01-04    16.850000    16.850000    16.850000    16.850000     1890000   \n",
              "1950-01-05    16.930000    16.930000    16.930000    16.930000     2550000   \n",
              "1950-01-06    16.980000    16.980000    16.980000    16.980000     2010000   \n",
              "1950-01-09    17.080000    17.080000    17.080000    17.080000     2520000   \n",
              "...                 ...          ...          ...          ...         ...   \n",
              "2022-09-06  3930.889893  3942.550049  3886.750000  3908.189941  2209800080   \n",
              "2022-09-07  3909.429932  3987.889893  3906.030029  3979.870117           0   \n",
              "2022-09-08  3959.939941  4010.500000  3944.810059  4006.179932           0   \n",
              "2022-09-09  4022.939941  4076.810059  4022.939941  4067.360107           0   \n",
              "2022-09-12  4083.669922  4119.279785  4083.669922  4107.279785  1602969000   \n",
              "\n",
              "            Dividends  Stock Splits  \n",
              "Date                                 \n",
              "1950-01-03          0             0  \n",
              "1950-01-04          0             0  \n",
              "1950-01-05          0             0  \n",
              "1950-01-06          0             0  \n",
              "1950-01-09          0             0  \n",
              "...               ...           ...  \n",
              "2022-09-06          0             0  \n",
              "2022-09-07          0             0  \n",
              "2022-09-08          0             0  \n",
              "2022-09-09          0             0  \n",
              "2022-09-12          0             0  \n",
              "\n",
              "[18292 rows x 7 columns]"
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "sp500"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "3e7ddd5b-9c2d-4c13-8210-72a4adb61159",
      "metadata": {
        "id": "3e7ddd5b-9c2d-4c13-8210-72a4adb61159",
        "outputId": "64ccfdfe-1abe-4466-fffe-85bc00e1b179"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<AxesSubplot:xlabel='Date'>"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "sp500.plot.line(y=\"Close\", use_index=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1b02b64d-9eef-489f-894d-26f9e6792db5",
      "metadata": {
        "id": "1b02b64d-9eef-489f-894d-26f9e6792db5"
      },
      "outputs": [],
      "source": [
        "del sp500[\"Dividends\"]\n",
        "del sp500[\"Stock Splits\"]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f25e1594-1cd2-47ae-bb50-a0d17ac35c69",
      "metadata": {
        "id": "f25e1594-1cd2-47ae-bb50-a0d17ac35c69"
      },
      "outputs": [],
      "source": [
        "sp500[\"Tomorrow\"] = sp500[\"Close\"].shift(-1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "871b16a1-9d77-40c8-8564-1947b438a113",
      "metadata": {
        "id": "871b16a1-9d77-40c8-8564-1947b438a113"
      },
      "outputs": [],
      "source": [
        "sp500[\"Target\"] = (sp500[\"Tomorrow\"] > sp500[\"Close\"]).astype(int)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "79e58626-3be6-45f7-b1aa-1786593e3bd6",
      "metadata": {
        "id": "79e58626-3be6-45f7-b1aa-1786593e3bd6"
      },
      "outputs": [],
      "source": [
        "sp500 = sp500.loc[\"1990-01-01\":].copy()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ad95d689-520a-4141-ab6e-a0fe3f9697a6",
      "metadata": {
        "id": "ad95d689-520a-4141-ab6e-a0fe3f9697a6",
        "outputId": "20e127de-0f18-4feb-840c-aaf1d3a1ec94"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "RandomForestClassifier(min_samples_split=100, random_state=1)"
            ]
          },
          "execution_count": 41,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "from sklearn.ensemble import RandomForestClassifier\n",
        "\n",
        "model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)\n",
        "\n",
        "train = sp500.iloc[:-100]\n",
        "test = sp500.iloc[-100:]\n",
        "\n",
        "predictors = [\"Close\", \"Volume\", \"Open\", \"High\", \"Low\"]\n",
        "model.fit(train[predictors], train[\"Target\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c0837787-5d4e-4a20-ad0d-3a546bc23cdb",
      "metadata": {
        "id": "c0837787-5d4e-4a20-ad0d-3a546bc23cdb",
        "outputId": "8374257b-1ad1-4256-a933-5faaa3722dbd"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.47058823529411764"
            ]
          },
          "execution_count": 42,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "from sklearn.metrics import precision_score\n",
        "\n",
        "preds = model.predict(test[predictors])\n",
        "preds = pd.Series(preds, index=test.index)\n",
        "precision_score(test[\"Target\"], preds)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e33e349f-8365-4282-91db-3b5824e83262",
      "metadata": {
        "id": "e33e349f-8365-4282-91db-3b5824e83262",
        "outputId": "1f587a83-65cc-43fa-f624-c34a445238ff"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<AxesSubplot:xlabel='Date'>"
            ]
          },
          "execution_count": 43,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXQAAAEECAYAAAA4Qc+SAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8/fFQqAAAACXBIWXMAAAsTAAALEwEAmpwYAACWhElEQVR4nO29ebxlV1km/Lxrn+HWvVWVoaoykEoICQEJg6ARRNTGgWZQQBERUBG1QVHQdmppGRSHT5T+0X7dggot0NpCvqA2YhsFG1CQMQECBEJICIQMZKpMVXc4w97r+2MNe8177X3Orapbtd/fLzl1zzl777X3Wfvdz3re531f4pyjt9566623nW/sWA+gt95666235Vjv0HvrrbfeThDrHXpvvfXW2wlivUPvrbfeejtBrHfovfXWW28niA2O1YH379/Pzz///GN1+N566623HWmf/OQn7+KcHwh9dswc+vnnn48rr7zyWB2+t956621HGhHdGPusp1x666233k4Q6x16b7311tsJYr1D76233no7Qax36L311ltvJ4g1OnQiegsR3UFEV0c+JyL6b0R0PRF9loi+afnD7K233nrrrclyEPrbADwl8flTAVwk/3sxgD9ZfFi99dZbb721tUbZIuf8g0R0fuIrzwTwF1yUbfwYEZ1KRGdzzr++rEFadsc1wK1XAY/8YaAYgHOOK756D77l/NNARMFNbrj647j7hk8BAM5+xHfinAseDgC4+45bcMPH/h5AvOLkoGB4xAP2YsDy2Kn1yRz3T2Y4e+8u630Ojq/ctY4L9u+Obnvb/VtYGxfYMx5a7x+ezHDtbYcBAKevjcL7GK4AD30aPvyV+3DH4S399in3XoNvXr0dp6wM/W0CVnGOrx6yx3nt7YdxeGsW/P4FB9Zw+urY/+C084HzHhc/0JffDxy5Ezffu4H9u8dYGRQAgNvu38RV7GJsrj4Ajzp4Ki48ELle5Qy49nLw2SauvvV+TGYlaDDCw5/4I1hZjWxz381ANRdjA4CNu4Hr34fJfIbP33I/qpaVRy88sBunrY5abWPaTfds4Iy9Y4yLIjzczRmuu0P87kfWHoh7Tn8Uztq7C4+/cB8AgFclrvvQO3HRqQAhPPdvvW8Tt967ab33gFN34QGn7Ap+37SvHDqC805bRZE595VNyhJ33D/BuaetAmv7UF7wPfi/19yO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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "combined = pd.concat([test[\"Target\"], preds], axis=1)\n",
        "combined.plot()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d4049497-0ee7-4399-83ab-ef61ccf71133",
      "metadata": {
        "id": "d4049497-0ee7-4399-83ab-ef61ccf71133"
      },
      "outputs": [],
      "source": [
        "def predict(train, test, predictors, model):\n",
        "    model.fit(train[predictors], train[\"Target\"])\n",
        "    preds = model.predict(test[predictors])\n",
        "    preds = pd.Series(preds, index=test.index, name=\"Predictions\")\n",
        "    combined = pd.concat([test[\"Target\"], preds], axis=1)\n",
        "    return combined"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ca97d93a-6841-49ef-8f91-25a713baef16",
      "metadata": {
        "id": "ca97d93a-6841-49ef-8f91-25a713baef16"
      },
      "outputs": [],
      "source": [
        "def backtest(data, model, predictors, start=2500, step=250):\n",
        "    all_predictions = []\n",
        "\n",
        "    for i in range(start, data.shape[0], step):\n",
        "        train = data.iloc[0:i].copy()\n",
        "        test = data.iloc[i:(i+step)].copy()\n",
        "        predictions = predict(train, test, predictors, model)\n",
        "        all_predictions.append(predictions)\n",
        "\n",
        "    return pd.concat(all_predictions)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8a75261f-d2de-4bc6-9364-54d520c63985",
      "metadata": {
        "id": "8a75261f-d2de-4bc6-9364-54d520c63985"
      },
      "outputs": [],
      "source": [
        "predictions = backtest(sp500, model, predictors)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "439d8704-c55d-4d1f-a709-acdc0f485e87",
      "metadata": {
        "id": "439d8704-c55d-4d1f-a709-acdc0f485e87",
        "outputId": "cd2e3d4b-7c32-4fdb-d0fc-a27dc349abfb"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0    3337\n",
              "1    2401\n",
              "Name: Predictions, dtype: int64"
            ]
          },
          "execution_count": 47,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "predictions[\"Predictions\"].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "bf105e8f-6be5-4494-9658-233761f1c4f4",
      "metadata": {
        "id": "bf105e8f-6be5-4494-9658-233761f1c4f4",
        "outputId": "2f1bb121-ec1b-4c8b-fc33-75dbf9d3582f"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.534777176176593"
            ]
          },
          "execution_count": 48,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "precision_score(predictions[\"Target\"], predictions[\"Predictions\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "eff25a20-375e-444a-b5d3-b558753fc817",
      "metadata": {
        "id": "eff25a20-375e-444a-b5d3-b558753fc817",
        "outputId": "9ac1fd2f-1c35-40fa-a413-ceac46433a44"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "1    0.536075\n",
              "0    0.463925\n",
              "Name: Target, dtype: float64"
            ]
          },
          "execution_count": 49,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "predictions[\"Target\"].value_counts() / predictions.shape[0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ed05ece5-f1f4-443a-b179-33c7e709ea4d",
      "metadata": {
        "id": "ed05ece5-f1f4-443a-b179-33c7e709ea4d"
      },
      "outputs": [],
      "source": [
        "horizons = [2,5,60,250,1000]\n",
        "new_predictors = []\n",
        "\n",
        "for horizon in horizons:\n",
        "    rolling_averages = sp500.rolling(horizon).mean()\n",
        "\n",
        "    ratio_column = f\"Close_Ratio_{horizon}\"\n",
        "    sp500[ratio_column] = sp500[\"Close\"] / rolling_averages[\"Close\"]\n",
        "\n",
        "    trend_column = f\"Trend_{horizon}\"\n",
        "    sp500[trend_column] = sp500.shift(1).rolling(horizon).sum()[\"Target\"]\n",
        "\n",
        "    new_predictors+= [ratio_column, trend_column]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "6c04ab2d-64ff-4f56-a206-605dcce30372",
      "metadata": {
        "id": "6c04ab2d-64ff-4f56-a206-605dcce30372"
      },
      "outputs": [],
      "source": [
        "sp500 = sp500.dropna(subset=sp500.columns[sp500.columns != \"Tomorrow\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fd7b2523-85a4-477d-975d-9cf64b1ff557",
      "metadata": {
        "id": "fd7b2523-85a4-477d-975d-9cf64b1ff557",
        "outputId": "561b516a-2973-4338-ea42-1d448f88ec64"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Open</th>\n",
              "      <th>High</th>\n",
              "      <th>Low</th>\n",
              "      <th>Close</th>\n",
              "      <th>Volume</th>\n",
              "      <th>Tomorrow</th>\n",
              "      <th>Target</th>\n",
              "      <th>Close_Ratio_2</th>\n",
              "      <th>Trend_2</th>\n",
              "      <th>Close_Ratio_5</th>\n",
              "      <th>Trend_5</th>\n",
              "      <th>Close_Ratio_60</th>\n",
              "      <th>Trend_60</th>\n",
              "      <th>Close_Ratio_250</th>\n",
              "      <th>Trend_250</th>\n",
              "      <th>Close_Ratio_1000</th>\n",
              "      <th>Trend_1000</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1993-12-14</th>\n",
              "      <td>465.730011</td>\n",
              "      <td>466.119995</td>\n",
              "      <td>462.459991</td>\n",
              "      <td>463.059998</td>\n",
              "      <td>275050000</td>\n",
              "      <td>461.839996</td>\n",
              "      <td>0</td>\n",
              "      <td>0.997157</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.996617</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.000283</td>\n",
              "      <td>32.0</td>\n",
              "      <td>1.028047</td>\n",
              "      <td>127.0</td>\n",
              "      <td>1.176082</td>\n",
              "      <td>512.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1993-12-15</th>\n",
              "      <td>463.059998</td>\n",
              "      <td>463.690002</td>\n",
              "      <td>461.839996</td>\n",
              "      <td>461.839996</td>\n",
              "      <td>331770000</td>\n",
              "      <td>463.339996</td>\n",
              "      <td>1</td>\n",
              "      <td>0.998681</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.995899</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.997329</td>\n",
              "      <td>32.0</td>\n",
              "      <td>1.025151</td>\n",
              "      <td>126.0</td>\n",
              "      <td>1.172676</td>\n",
              "      <td>512.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1993-12-16</th>\n",
              "      <td>461.859985</td>\n",
              "      <td>463.980011</td>\n",
              "      <td>461.859985</td>\n",
              "      <td>463.339996</td>\n",
              "      <td>284620000</td>\n",
              "      <td>466.380005</td>\n",
              "      <td>1</td>\n",
              "      <td>1.001621</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.999495</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.000311</td>\n",
              "      <td>32.0</td>\n",
              "      <td>1.028274</td>\n",
              "      <td>127.0</td>\n",
              "      <td>1.176163</td>\n",
              "      <td>513.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1993-12-17</th>\n",
              "      <td>463.339996</td>\n",
              "      <td>466.380005</td>\n",
              "      <td>463.339996</td>\n",
              "      <td>466.380005</td>\n",
              "      <td>363750000</td>\n",
              "      <td>465.850006</td>\n",
              "      <td>0</td>\n",
              "      <td>1.003270</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.004991</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.006561</td>\n",
              "      <td>32.0</td>\n",
              "      <td>1.034781</td>\n",
              "      <td>128.0</td>\n",
              "      <td>1.183537</td>\n",
              "      <td>514.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1993-12-20</th>\n",
              "      <td>466.380005</td>\n",
              "      <td>466.899994</td>\n",
              "      <td>465.529999</td>\n",
              "      <td>465.850006</td>\n",
              "      <td>255900000</td>\n",
              "      <td>465.299988</td>\n",
              "      <td>0</td>\n",
              "      <td>0.999431</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.003784</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.005120</td>\n",
              "      <td>32.0</td>\n",
              "      <td>1.033359</td>\n",
              "      <td>128.0</td>\n",
              "      <td>1.181856</td>\n",
              "      <td>513.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-06</th>\n",
              "      <td>3930.889893</td>\n",
              "      <td>3942.550049</td>\n",
              "      <td>3886.750000</td>\n",
              "      <td>3908.189941</td>\n",
              "      <td>2209800080</td>\n",
              "      <td>3979.870117</td>\n",
              "      <td>1</td>\n",
              "      <td>0.997948</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.989893</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.982136</td>\n",
              "      <td>26.0</td>\n",
              "      <td>0.902791</td>\n",
              "      <td>120.0</td>\n",
              "      <td>1.103594</td>\n",
              "      <td>542.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-07</th>\n",
              "      <td>3909.429932</td>\n",
              "      <td>3987.889893</td>\n",
              "      <td>3906.030029</td>\n",
              "      <td>3979.870117</td>\n",
              "      <td>0</td>\n",
              "      <td>4006.179932</td>\n",
              "      <td>1</td>\n",
              "      <td>1.009087</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.008370</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.999819</td>\n",
              "      <td>27.0</td>\n",
              "      <td>0.919786</td>\n",
              "      <td>121.0</td>\n",
              "      <td>1.123489</td>\n",
              "      <td>543.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-08</th>\n",
              "      <td>3959.939941</td>\n",
              "      <td>4010.500000</td>\n",
              "      <td>3944.810059</td>\n",
              "      <td>4006.179932</td>\n",
              "      <td>0</td>\n",
              "      <td>4067.360107</td>\n",
              "      <td>1</td>\n",
              "      <td>1.003294</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.012411</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.005349</td>\n",
              "      <td>28.0</td>\n",
              "      <td>0.926253</td>\n",
              "      <td>122.0</td>\n",
              "      <td>1.130564</td>\n",
              "      <td>543.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-09</th>\n",
              "      <td>4022.939941</td>\n",
              "      <td>4076.810059</td>\n",
              "      <td>4022.939941</td>\n",
              "      <td>4067.360107</td>\n",
              "      <td>0</td>\n",
              "      <td>4107.279785</td>\n",
              "      <td>1</td>\n",
              "      <td>1.007578</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.022676</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.019287</td>\n",
              "      <td>29.0</td>\n",
              "      <td>0.940748</td>\n",
              "      <td>122.0</td>\n",
              "      <td>1.147454</td>\n",
              "      <td>543.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-12</th>\n",
              "      <td>4083.669922</td>\n",
              "      <td>4119.279785</td>\n",
              "      <td>4083.669922</td>\n",
              "      <td>4107.279785</td>\n",
              "      <td>1602969000</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>1.004883</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.023296</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.027929</td>\n",
              "      <td>29.0</td>\n",
              "      <td>0.950276</td>\n",
              "      <td>123.0</td>\n",
              "      <td>1.158331</td>\n",
              "      <td>543.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>7238 rows × 17 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                   Open         High          Low        Close      Volume  \\\n",
              "Date                                                                         \n",
              "1993-12-14   465.730011   466.119995   462.459991   463.059998   275050000   \n",
              "1993-12-15   463.059998   463.690002   461.839996   461.839996   331770000   \n",
              "1993-12-16   461.859985   463.980011   461.859985   463.339996   284620000   \n",
              "1993-12-17   463.339996   466.380005   463.339996   466.380005   363750000   \n",
              "1993-12-20   466.380005   466.899994   465.529999   465.850006   255900000   \n",
              "...                 ...          ...          ...          ...         ...   \n",
              "2022-09-06  3930.889893  3942.550049  3886.750000  3908.189941  2209800080   \n",
              "2022-09-07  3909.429932  3987.889893  3906.030029  3979.870117           0   \n",
              "2022-09-08  3959.939941  4010.500000  3944.810059  4006.179932           0   \n",
              "2022-09-09  4022.939941  4076.810059  4022.939941  4067.360107           0   \n",
              "2022-09-12  4083.669922  4119.279785  4083.669922  4107.279785  1602969000   \n",
              "\n",
              "               Tomorrow  Target  Close_Ratio_2  Trend_2  Close_Ratio_5  \\\n",
              "Date                                                                     \n",
              "1993-12-14   461.839996       0       0.997157      1.0       0.996617   \n",
              "1993-12-15   463.339996       1       0.998681      0.0       0.995899   \n",
              "1993-12-16   466.380005       1       1.001621      1.0       0.999495   \n",
              "1993-12-17   465.850006       0       1.003270      2.0       1.004991   \n",
              "1993-12-20   465.299988       0       0.999431      1.0       1.003784   \n",
              "...                 ...     ...            ...      ...            ...   \n",
              "2022-09-06  3979.870117       1       0.997948      0.0       0.989893   \n",
              "2022-09-07  4006.179932       1       1.009087      1.0       1.008370   \n",
              "2022-09-08  4067.360107       1       1.003294      2.0       1.012411   \n",
              "2022-09-09  4107.279785       1       1.007578      2.0       1.022676   \n",
              "2022-09-12          NaN       0       1.004883      2.0       1.023296   \n",
              "\n",
              "            Trend_5  Close_Ratio_60  Trend_60  Close_Ratio_250  Trend_250  \\\n",
              "Date                                                                        \n",
              "1993-12-14      1.0        1.000283      32.0         1.028047      127.0   \n",
              "1993-12-15      1.0        0.997329      32.0         1.025151      126.0   \n",
              "1993-12-16      2.0        1.000311      32.0         1.028274      127.0   \n",
              "1993-12-17      3.0        1.006561      32.0         1.034781      128.0   \n",
              "1993-12-20      2.0        1.005120      32.0         1.033359      128.0   \n",
              "...             ...             ...       ...              ...        ...   \n",
              "2022-09-06      1.0        0.982136      26.0         0.902791      120.0   \n",
              "2022-09-07      2.0        0.999819      27.0         0.919786      121.0   \n",
              "2022-09-08      3.0        1.005349      28.0         0.926253      122.0   \n",
              "2022-09-09      3.0        1.019287      29.0         0.940748      122.0   \n",
              "2022-09-12      4.0        1.027929      29.0         0.950276      123.0   \n",
              "\n",
              "            Close_Ratio_1000  Trend_1000  \n",
              "Date                                      \n",
              "1993-12-14          1.176082       512.0  \n",
              "1993-12-15          1.172676       512.0  \n",
              "1993-12-16          1.176163       513.0  \n",
              "1993-12-17          1.183537       514.0  \n",
              "1993-12-20          1.181856       513.0  \n",
              "...                      ...         ...  \n",
              "2022-09-06          1.103594       542.0  \n",
              "2022-09-07          1.123489       543.0  \n",
              "2022-09-08          1.130564       543.0  \n",
              "2022-09-09          1.147454       543.0  \n",
              "2022-09-12          1.158331       543.0  \n",
              "\n",
              "[7238 rows x 17 columns]"
            ]
          },
          "execution_count": 55,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "sp500"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "283be581-dbe1-4f02-8851-ff1a027b4104",
      "metadata": {
        "id": "283be581-dbe1-4f02-8851-ff1a027b4104"
      },
      "outputs": [],
      "source": [
        "model = RandomForestClassifier(n_estimators=200, min_samples_split=50, random_state=1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "a843303c-a247-4f6d-9505-cc711ca95afa",
      "metadata": {
        "id": "a843303c-a247-4f6d-9505-cc711ca95afa"
      },
      "outputs": [],
      "source": [
        "def predict(train, test, predictors, model):\n",
        "    model.fit(train[predictors], train[\"Target\"])\n",
        "    preds = model.predict_proba(test[predictors])[:,1]\n",
        "    preds[preds >=.6] = 1\n",
        "    preds[preds <.6] = 0\n",
        "    preds = pd.Series(preds, index=test.index, name=\"Predictions\")\n",
        "    combined = pd.concat([test[\"Target\"], preds], axis=1)\n",
        "    return combined"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "fb820946-1275-4914-b6a8-355e96f315b6",
      "metadata": {
        "id": "fb820946-1275-4914-b6a8-355e96f315b6"
      },
      "outputs": [],
      "source": [
        "predictions = backtest(sp500, model, new_predictors)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "a73e1816-283a-47ac-af43-4550b80307ef",
      "metadata": {
        "id": "a73e1816-283a-47ac-af43-4550b80307ef",
        "outputId": "96624c0b-eb3e-4905-b5bd-c78967121660"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.0    3933\n",
              "1.0     805\n",
              "Name: Predictions, dtype: int64"
            ]
          },
          "execution_count": 59,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "predictions[\"Predictions\"].value_counts()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "14acc336-4991-4189-bb16-4a8bf53056e1",
      "metadata": {
        "id": "14acc336-4991-4189-bb16-4a8bf53056e1",
        "outputId": "1cdb9df0-cc5c-48f6-88d7-ee98461325ef"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.5701863354037268"
            ]
          },
          "execution_count": 60,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "precision_score(predictions[\"Target\"], predictions[\"Predictions\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "21b3d365-2157-4229-a785-ae687da0f21f",
      "metadata": {
        "id": "21b3d365-2157-4229-a785-ae687da0f21f",
        "outputId": "faa7e627-8c92-4b3c-c3b6-40b5b16ea8b0"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "1    0.546855\n",
              "0    0.453145\n",
              "Name: Target, dtype: float64"
            ]
          },
          "execution_count": 61,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "predictions[\"Target\"].value_counts() / predictions.shape[0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ef08fff5-0dd5-4d86-9d0d-8ce9f7443865",
      "metadata": {
        "id": "ef08fff5-0dd5-4d86-9d0d-8ce9f7443865",
        "outputId": "7464bdcc-84b2-4498-c11a-3e2fe33e7d24"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Target</th>\n",
              "      <th>Predictions</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2003-11-14</th>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2003-11-17</th>\n",
              "      <td>0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2003-11-18</th>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2003-11-19</th>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2003-11-20</th>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-06</th>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-07</th>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-08</th>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-09</th>\n",
              "      <td>1</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2022-09-12</th>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>4738 rows × 2 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "            Target  Predictions\n",
              "Date                           \n",
              "2003-11-14       0          0.0\n",
              "2003-11-17       0          1.0\n",
              "2003-11-18       1          1.0\n",
              "2003-11-19       0          0.0\n",
              "2003-11-20       1          1.0\n",
              "...            ...          ...\n",
              "2022-09-06       1          0.0\n",
              "2022-09-07       1          0.0\n",
              "2022-09-08       1          0.0\n",
              "2022-09-09       1          0.0\n",
              "2022-09-12       0          0.0\n",
              "\n",
              "[4738 rows x 2 columns]"
            ]
          },
          "execution_count": 62,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "predictions"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b2d35fd3-7038-4e69-bcbd-bde42c1f5e33",
      "metadata": {
        "id": "b2d35fd3-7038-4e69-bcbd-bde42c1f5e33"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.13"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}