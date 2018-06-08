function sendData (evt) {
    evt.preventDefault()

    weight = $('#weight').val()
    reps = $('#reps').val()
    week = $('#week').val()

    console.log(week)

    let formInputs = {'weight': weight, 'reps': reps, 'week': week}

    $.get('/calculate-next-rep-max', formInputs, displayRepMax)
}

function displayRepMax (response) {

    $('#plan').html('')

    for (let plan of response.weights) {
        $('#plan').append(`<b>Reps:</b> ${plan[1]}   <b>Weight:</b> ${plan[0]}   <b>New Max:</b> ${plan[2]}<br>`)
    }
}


$('#next-max').on('submit', sendData)

