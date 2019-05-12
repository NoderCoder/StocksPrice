import bs4
import requests as rq
"""
@author : NoderCoder

"""
Stocks =[ 'AMZN','FB','BEMG']

def FetchPrice(ticker):
    """
    Enter ticker and based on the that the function returns the values of the stock
    Might experiment with GUI and API late to make this Faster
    """
    url = 'https://finance.yahoo.com/quote/'+ticker+'?p='+ticker
    r = rq.get(url)
    soup = bs4.BeautifulSoup(r.text,"xml")
    price_soup = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})#[0].find('span')

    #converting the soup tag object into string
    Temp_string = []
    for x in price_soup:
        Temp_string.append(str(x))
    ps: str = Temp_string[0]

    # Looking for price
    p_i_1: int = ps.find('data-reactid="14">')
    p_i_2: int = ps.find('</span><div class="D(ib) Va(t)')
    p_v = ps[(p_i_1 + 18):p_i_2]

    # looking for price change
    pc_i_1: int = ps.find('data-reactid="16">')
    pc_i_2: int = ps.find('</span><div class="Fw(n) C($c-fuji-grey-j)')
    p_c = ps[(pc_i_1 + 18):pc_i_2]

    # looking for time
    pt_i_1: int = ps.find('data-reactid="18">At close:')
    pt_i_2: int = ps.find('EDT</span></div></div><!-- react-empty: 19')
    p_t = ps[(pt_i_1 + 18):pt_i_2]
    op_list = [ticker,p_v,p_c,p_t]
    return op_list
for i in Stocks:
    print('the function value is',FetchPrice(i))