var a = [];
var b = [];
for(i = 0; i < 10; i++)
{
    a[i] = Math.random();
    b[i] = Math.random();
}

console.log("<!DOCTYPE html>");
console.log("<html>");
console.log("<body>");
console.log("<p>Two randomly generated arrays:</p>");
console.log("\t<table border=1>");
console.log("\t\t<tr>");
console.log("\t\t\t<td>");
console.log("\t\t\ti");
console.log("\t\t\t</td>");
console.log("\t\t\t<td>");
console.log("\t\t\ta[i]");
console.log("\t\t\t</td>");
console.log("\t\t\t<td>");
console.log("\t\t\tb[i]");
console.log("\t\t\t</td>");

for(i = 0; i < a.length; i++)
{
    console.log("\t\t<tr>");
    console.log("\t\t\t<td>");
    console.log("\t\t\t", i);
    console.log("\t\t\t</td>");
    console.log("\t\t\t<td>");
    console.log("\t\t\t", a[i]);
    console.log("\t\t\t</td>");
    console.log("\t\t\t<td>");
    console.log("\t\t\t", b[i]);
    console.log("\t\t\t</td>");
    console.log("\t\t</tr>");
}

console.log("\t</table>");
console.log("</body>");
console.log("</html>");
