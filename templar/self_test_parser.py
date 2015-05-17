from bs4 import BeautifulSoup

OPTION_DELIMITER = ' ||| '

QUIZ_TEMPLATE =  """<div class="self-test">
                        <table class="question">
                        </table>
                        <div class="testbutton checkbutton">Check Solution</div>
                    </div>"""

ITEM_TEMPLATE =  """<tr>
                        <td><input type="radio" name="q0"></td>
                        <td><div class="text">{{ answer }}</div></td>
                        <td>
                            <div class="text">
                                {{ explanation }}
                            </div>
                        </td>
                    </tr>"""

def create_self_test_html(html_text):
    '''
    Takes a series of bullet points in html and turns them into a table of 
    multiple choice questions. The multiple choice question format is 
    courtesy of Sarah Kim.
    '''
    quiz_soup = BeautifulSoup(QUIZ_TEMPLATE)
    input_soup = BeautifulSoup(html_text)
    bullet_points = input_soup.ul.find_all('li', recursive=False)
    for point in bullet_points:
        item_text = str(point)
        item_text = item_text.strip('<li>')
        item_text = item_text.strip('</li>')
        answer, explanation = item_text.split(OPTION_DELIMITER)
        item = ITEM_TEMPLATE.replace('{{ answer }}', answer)
        item = item.replace('{{ explanation }}', explanation)
        item_soup = BeautifulSoup(item)
        quiz_soup.div.table.contents.append(item_soup.tr)
    return quiz_soup.html.div.prettify()