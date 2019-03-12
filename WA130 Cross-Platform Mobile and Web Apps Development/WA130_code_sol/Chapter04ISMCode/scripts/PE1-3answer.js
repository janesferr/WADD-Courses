function setup() {
  document.getElementById("gallons").onclick =
    function () {
      setUnits("L");
    };
  document.getElementById("litres").onclick =
    function () {
      setUnits("G");
    };
}

function setUnits(unit) {
  var label = document.getElementById("label");
  label.innerHTML = " " + unit;
}

function validate(value) {
  if (document.getElementById("litres").checked) {
    if (value > 1000) {
      alert('You must enter a value less than 1000 Gallons');
    }
  } else {
    if (value > 4000) {
      alert('You must enter a value less than 4000 Litres');
    }
  }
}

function convert() {
  var litresButton = document.getElementById("litres");
  var fluid = document.getElementById("fluid");
  validate(fluid.value);
  if (litresButton.checked) {
    convertToLitres(fluid.value);
  } else {
    convertToGallons(fluid.value);
  }
}

function convertToLitres(fluidInGallons) {
  var litresFluid = fluidInGallons / 0.26417; // US Gallons
  // var litresFluid = fluidInGallons / 0.21997; // Imperial Gallons
  document.getElementById("answer").innerHTML =
    fluidInGallons +
    " Gallons converts to " +
    litresFluid.toFixed(1) +
    " Litres";
}

function convertToGallons(fluidInLitres) {
  var gallonsFluid = fluidInLitres * 0.25417; // US Gallons
  // var gallonsFluid = fluidInLitres * 0.21997 // Imperial Gallons
  document.getElementById("answer").innerHTML =
    fluidInLitres +
    " Litres converts to " +
    gallonsFluid.toFixed(1) +
    " Gallons";
}