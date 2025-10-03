from django.shortcuts import render

# Create your views here.
def temperature_converter(request):
    """
    Temperature converter view that handles both GET and POST requests
    """
    result = None
    input_temp = None
    output_unit = None
    
    if request.method == 'POST':
        try:
            input_temp = float(request.POST.get('numInput', 0))
            input_unit = request.POST.get('input_type', 'Celsius')
            output_unit = request.POST.get('output_type', 'Fahrenheit')
            
            # First convert input to Celsius as base
            if input_unit == 'Celsius':
                celsius = input_temp
            elif input_unit == 'Fahrenheit':
                celsius = (input_temp - 32) * 5 / 9
            elif input_unit == 'Kelvin':
                celsius = input_temp - 273.15
            else:
                celsius = input_temp
            
            # Then convert from Celsius to output unit
            if output_unit == 'Celsius':
                result = celsius
            elif output_unit == 'Fahrenheit':
                result = celsius * 9 / 5 + 32
            elif output_unit == 'Kelvin':
                result = celsius + 273.15
            
            result = round(result, 2)
            
        except (ValueError, TypeError):
            result = "Invalid input"
    
    context = {
        'result': result,
        'input_temp': input_temp,
        'output_unit': output_unit,
    }
    
    return render(request, 'Home.html', context)
