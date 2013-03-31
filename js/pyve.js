$(function () {
    var membersURL = "https://api.github.com/orgs/pyve/members";
    var lista = $("#lista_pythonistas");

    var getPyVeMembers = function () {
        $.getJSON(membersURL).then(function (data) {
            $.each(data, function (i) {
                var content = "<div class=\"span2 text-center img-polaroid\"><a href=\"" + data[i]["html_url"] + "\">" + "<img src=\"" + data[i]["avatar_url"] + "\" class=\"img-polaroid\" /><br>" + data[i]["login"] + "</a></div>";
                lista.append(content);
            });
        });
    };
    $(document).ready(function() {
        getPyVeMembers();
    });
});
