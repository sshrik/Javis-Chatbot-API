Javis-Chatbot-API
This repository is derived with Weather Bot(https://github.com/sshrik/WeatherBot).

This API is aim to...
1. Easy to using.
2. Conversation teach helper with tagging like google SyntaxNet.

But our tagging is not word`s role at sentence, but simple meaning at sentence. We can think it like variable of program.



DB Schema ( MongoDB )
1.SignIn Schema
{
    "id" : string,
    "key" : string,
    "teachNumber" : int
}

2.Conversation Schema
{
    "input" : string,
    "output" : [string]
}

3.Word Sechema
{
    "word" : string,
    "tag" : [string]
}

4.Sentence Sechema
{
    "sentence" : string,
    "tag" : [string]
}

5.wtag Sechema
{
    "tag" : string,
    "word" : [string]
}

6.stag Sechema
{
    "tag" : string,
    "sentence" : [string]
}

7.tag2Many Sechema
{
    "inputTag" : string,
    "outputTag" : [string]
}

8.tag2one Sechema
{
    "inputTag" : [string],
    "outputTag" : string
}
