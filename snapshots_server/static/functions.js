$(document).ready(function(){
    setInterval(() => {
        $.ajax({
            type: 'GET',
            url: "/version",
            success:function(data){
                $('.snapshot_out_file').each(function(i, obj) {
                    $(this).text(data);
                });
            }
        });
    }, 3000); // Every 30 seconds retrieve current snapshot name
});