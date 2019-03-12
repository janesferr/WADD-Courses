function distance(a, b) {
    var sum = 0;
    for (i = 0; i < a.length; i++) {
        sum += Math.pow(a[i] - b[i], 2);
    }
    return Math.sqrt(sum) / a.length;
}

var a = [];
var b = [];
for(i = 0; i < 10; i++)
{
    a[i] = Math.random();
    b[i] = Math.random();
}

print("<!DOCTYPE html>");
print("<html>");
print("<body>");
print("<p>Two randomly generated arrays:</p>");
print("\t<table border=1>");
print("\t\t<tr>");
print("\t\t\t<td>");
print("\t\t\ti");
print("\t\t\t</td>");
print("\t\t\t<td>");
print("\t\t\ta[i]");
print("\t\t\t</td>");
print("\t\t\t<td>");
print("\t\t\tb[i]");
print("\t\t\t</td>");

for(i = 0; i < a.length; i++)
{
    print("\t\t<tr>");
    print("\t\t\t<td>");
    print("\t\t\t", i);
    print("\t\t\t</td>");
    print("\t\t\t<td>");
    print("\t\t\t", a[i]);
    print("\t\t\t</td>");
    print("\t\t\t<td>");
    print("\t\t\t", b[i]);
    print("\t\t\t</td>");
    print("\t\t</tr>");
}

print("\t</table>");
print("<p>");
print("\tThe distance between the arrays is: ", distance(a, b));
print("</p>");
print("</body>");
print("</html>");
