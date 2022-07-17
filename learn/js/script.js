

var date = Date()


function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}
  
sleep(500).then(() => {
    // Do something after the sleep!

    var date2 = Date()
});




console.log("DATE ", date)
console.log("DATE ", date2)



if( date == date2){
    console.log("THE SAME")

}else{
    console.log("NOT THE SAME")
}
