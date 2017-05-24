from flask import Flask, render_template, request
app = Flask(__name__)

my_text = []
bot = ["Hello there, please chat to me"]

def convert_to_text(bot, my_text):
    """
    return html code representing bot and my_text information
    """
    def add_style(text, id_col):
        if len(text) > 0:
            return """<p id="{}style">{}</p>""".format(id_col, text)
        return ""
    
    bot1 = bot[:]
    my_text1 = my_text[:]
    if len(bot1) != len(my_text1):
        my_text1.append("")
    
    chat_text = ["{} {}".format(add_style(x, "bot"), add_style(y, "my")) for x,y in zip(bot1, my_text1)]
    
    return "\n".join(chat_text)

def bot_action(text):
    text = "length of input text: {}".format(len(text))
    return text

@app.route('/', methods=['GET', 'POST'])
def my_bot():
    if request.method == "POST":
        my_response = request.form['reply_text']
        bot_response = bot_action(my_response)
        my_text.append(my_response)
        bot.append(bot_response)
    
    template_info = {
        'chat': convert_to_text(bot, my_text)
    }        
    return render_template('index.html', **template_info)

if __name__ == '__main__':
    app.run(debug=True)