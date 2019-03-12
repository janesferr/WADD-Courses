function draw() {
  var canvas = document.getElementById("canvasElement");
  var canvasContext = canvas.getContext("2d");

  var xCenter = 150;
  var yCenter1 = 50;
  var yCenter2 = 200;
  var width = 250;
  var height = 50;
  var ovalColor1 = "#9BBB59";
  var ovalColor2 = "#8064A2";

  canvasContext.strokeStyle = "#F2F2F2";
  canvasContext.lineWidth = 3;
  drawOval(canvasContext, xCenter, yCenter1, width, height, ovalColor1);
  drawOval(canvasContext, xCenter, yCenter2, width, height, ovalColor2);

  canvasContext.strokeStyle = "#000";
  canvasContext.lineWidth = 1;
  drawLine(canvasContext, xCenter - width / 2, yCenter1, xCenter - width / 2, yCenter2);
  drawLine(canvasContext, xCenter + width / 2, yCenter1, xCenter + width / 2, yCenter2);
}

function drawLine(canvasContext, lineStartX, lineStartY, lineEndX, lineEndY)
{
  canvasContext.beginPath();
  canvasContext.moveTo(lineStartX, lineStartY);
  canvasContext.lineTo(lineEndX, lineEndY);
  canvasContext.stroke();
}

// x, y are the coordinates of the center of the oval
function drawOval(canvasContext, xCenter, yCenter, width, height, fillColor) {
  canvasContext.beginPath();
  canvasContext.moveTo(xCenter - width / 2, yCenter);
  
  // Bottom half
  canvasContext.save();
  canvasContext.shadowBlur = 5;
  canvasContext.shadowOffsetY = 5;
  canvasContext.shadowColor = "#000";
  canvasContext.bezierCurveTo(xCenter - width / 2, yCenter + height / 2,
                              xCenter + width / 2, yCenter + height/ 2,
                              xCenter + width / 2, yCenter);
  canvasContext.stroke();
  
  // Top half
  canvasContext.restore();
  canvasContext.bezierCurveTo(xCenter + width / 2, yCenter - height / 2,
                              xCenter - width / 2, yCenter - height / 2,
                              xCenter - width / 2, yCenter);
  canvasContext.fillStyle = fillColor;
  canvasContext.fill();
  canvasContext.stroke();
}