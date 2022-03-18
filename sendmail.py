import yagmail


def mailReport(msg):
    yag = yagmail.SMTP('at14k3r@gmail.com', 'at14k3r@123')
    # receiver="vikashkumar990523@gmail.com"
    receiver="aliashhar3@gmail.com"
    # body = "Hello there from Yagmail"
    body = msg
    filename = "report.pdf"
    # print(filename)
    contents = [
        "This is the body, and here is just text http://somedomain/image.png",
        "You can find an audio file attached.", '/local/path/to/song.mp3'
    ]
    yag.send(
        to=receiver,
        subject="Yagmail test with attachment",
        contents=body, 
        attachments=filename,
    )