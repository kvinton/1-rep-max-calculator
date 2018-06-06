function sendData (evt) {
    evt.preventDefault()

    weight = $('#weight').val()
    reps = $('#reps').val()

    let formInputs = {'weight': weight, 'reps': reps}

    $.get('/calculate-rep-max', formInputs, displayRepMax)
}

function displayRepMax (response) {

    $('#rep-max').html(`${response} lbs`)
}



$('#rep-max-form').on('submit', sendData)

function sendWeightData (evt) {
    evt.preventDefault()

    target_max = $('#target-max').val()
    reps = $('#reps2').val()

    let formInputs = {'target-max': target_max, 'reps': reps}

    $.get('/calculate-working-weight', formInputs, displayWeight)

}

function displayWeight (response) {
    $('#working-weight').html(`${response} lbs`)
}


$('#weight-form').on('submit', sendWeightData)