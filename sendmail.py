import reportgeneration
import yagmail


yag = yagmail.SMTP('sender@gmail.com', 'senderPass')
# receiver="vikashkumar990523@gmail.com"
receiver="receiver@gmail.com"
body = "Hello there from Yagmail"
filename = reportgeneration.reportGenerator()
print(filename)
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