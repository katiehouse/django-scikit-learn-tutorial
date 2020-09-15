from django.shortcuts import render
from .forms import ModelForm
from .models import Predictions
import pickle


def predict_model(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            sepal_length = form.cleaned_data['sepal_length']
            sepal_width = form.cleaned_data['sepal_width']
            petal_length = form.cleaned_data['petal_length']
            petal_width = form.cleaned_data['petal_width']

            # Run new features through ML model
            model_features = [
                [sepal_length, sepal_width, petal_length, petal_width]]
            loaded_model = pickle.load(
                open("ml_model/iris_model.pkl", 'rb'))
            prediction = loaded_model.predict(model_features)[0]

            prediction_dict = [{'name': 'setosa',
                                'img': 'https://alchetron.com/cdn/iris-setosa-0ab3145a-68f2-41ca-a529-c02fa2f5b02-resize-750.jpeg'},
                               {'name': 'versicolor',
                                'img': 'https://wiki.irises.org/pub/Spec/SpecVersicolor/iversicolor07.jpg'},
                               {'name': 'virginica',
                                'img': 'https://www.gardenia.net/storage/app/public/uploads/images/detail/xUM027N8JI22aQPImPoH3NtIMpXkm89KAIKuvTMB.jpeg'}]

            prediction_name = prediction_dict[prediction]['name']
            prediction_img = prediction_dict[prediction]['img']

            # Save prediction to database Predictions table
            Predictions.objects.create(sepal_length=sepal_length,
                                       sepal_width=sepal_width,
                                       petal_length=petal_length,
                                       petal_width=petal_width,
                                       prediction=prediction_name)

            return render(request, 'home.html', {'form': form, 'prediction': prediction,
                                                 'prediction_name': prediction_name,
                                                 'prediction_img': prediction_img})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm()

    return render(request, 'home.html', {'form': form})
