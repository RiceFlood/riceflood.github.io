function generateURL(sensorNum,startDate,endDate){
    let url = 'https://api.thingspeak.com/channels/'
    let channels = {
        "1": "824825",
        "2": "824835",
        "3": "824849",
        "4": "824853",
        "5": "842071",
        "6": "842072",
        "7": "842073",
        "8": "842074"
    }
    let api = {
        "1": "D2C6ZRLUY4RYOS2V",
        "2": "U8LLWGVU0UIO9C9V",
        "3": "9BNF3MHPLN39MCDB",
        "4": "BOV93BV4CPEUOVWX",
        "5": "NR3KNWN07B7PU7PJ",
        "6": "OKMCXRC6884OKMPC",
        "7": "4PAELGVIXKM0GMN8",
        "8": "H37G5UKC6OCK0NI4"
    }
    return `https://api.thingspeak.com/channels/${channels[sensorNum]}/charts/1?api_key=${api[sensorNum]}&start=${startDate}%2005:00:00&end=${endDate}%2005:00:00&width=1600&step=true&dynamic=true&update=5`;
}
$("#refreshIframe").click(()=>{
    $('#iframeGraph').attr("src",generateURL($('#sensorNum').val(),$('#startDate').val(),$('#endDate').val()));
})