Dim Title, Message, MsgResult

Title = "VBX"
Message = "SUCKAH"

Do
    MsgResult = MsgBox(Message, vbOKOnly + vbCritical, Title)
Loop While MsgResult = vbOK
