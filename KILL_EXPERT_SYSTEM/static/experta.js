function calculate(){

    skills = {

        skill1: $("#skill1").val(),
        skill2: $("#skill2").val(),
        skill3: $("#skill3").val(),
        skill4: $("#skill4").val(),
        skill5: $("#skill5").val(),
        skill6: $("#skill6").val(),
        skill7: $("#skill7").val(),
        skill8: $("#skill8").val(),
        skill9: $("#skill9").val(),
        skill10: $("#skill10").val(),
        skill11: $("#skill11").val(),
        skill12: $("#skill12").val(),
        skill13: $("#skill13").val(),
        skill14: $("#skill14").val(),
        skill15: $("#skill15").val(),
    }

    $.ajax({
        type: 'GET',
        url: '/calculate-skills',
        data:  skills,
        dataType: "json",
        success: function(result){
            console.log(result)
            alert("Success!")

            Object.keys(result).forEach(function (order){

                $('#resultDiv').append(
                    `<p style="margin:0 0 0.5rem 0; font-size: 0.9rem;">${order} :<span style="color: green;"> ${result[order]* 10 + '%'}</span></p>`
                )
            })
        }
    })
}