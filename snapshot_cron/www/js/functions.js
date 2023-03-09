var snapshot_filename = 'snapshot-0076278b328f748d88dff1ec5b48d088eb0831304e00571a374a78f8c72b0455.bin';
var webpage_url = '<web page url>/snaps/';
$(document).ready(function(){
    $(".snapshot_out_file").each(function(obj, val){
        $(this).text("curl -k " + webpage_url + snapshot_filename + " -o " + snapshot_filename);
    });
    $(".snapshot_download_link").each(function(obj, val){
        $(this).attr("href", webpage_url + snapshot_filename);
    });
});