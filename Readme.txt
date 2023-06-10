INSTALLATION

Visual Studio Code
1.Download the Visual Studio Code installer for Windows.
2.Once it is downloaded, run the installer (VSCodeUserSetup-{version}.exe). This will only take a minute.
3.By default, VS Code is installed under C:\Users\{Username}\AppData\Local\Programs\Microsoft VS Code.



TECH STACKS:

1) HTML:
  Hyper Text Markup Language is a markup language used to design static web pages.

2) CSS
  Cascading Style Sheet is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.  

3) JAVASCRIPT
  JavaScript, often abbreviated as JS, is a Programming language that is one of the technologies of the World Wide Web, alongside HTML and CSS.

4) Python
  Python is a high-level, general-purpose Programming Language. 

5) Flask
  for creating web applications.  We are using Flask Framework, the communication between each respective module were 
  handled by Request and Response libraries with Synchronous calls.

6) Anaconda 
    for Python + useful packages.


7) Web Scraping: For Product comparison, price comparison, and QR-based comparison. 
  Web scraping is a process of automating the extraction of data in an efficient and fast way. With the help of web scraping, we are extracting data from websites like snapdeal and flipkart.

8) Computer Vision: For QR based authentication and QR based comparison.
   Computer vision is a field of artificial intelligence (AI) that enables computers and systems to derive meaningful information from digital images, videos and other visual inputs — and take actions or make recommendations based on that information.

9) Libraries used:
   1. Beautiful Soup, Scrappy and Selenium for Web Scraping.
   2. Pyzbar, Cv2, Types for computer vision and steganography.
   3. NumPy, Matplotlib and Pandas for data analysis and recommendation engines.

These Libraries also helps in getting input values form the user/client and sending response back to it from System/server. We use self-developed bot to scrape various other ecommerce websites like Flipkart, Snapdeal etc. using Scrappy, Selenium and bs4 libraries. For connecting to internet, we used libraries like Web browser and Requests.



TO RUN A PROJECT :


First Install all the Requirements: -

pip install -r requirements.txt

To run Project: -

python FreeCom.py


OVERVIEW-


PROBLEM:  

Since the usage of the internet is growing day by day, many of the daily necessary products are available online on e-commerce websites. By knowing the demand of the customers, there aremany e-commerce websites that are selling the same product but at different prices. This pricevariation is dependent on various factors, such as offers, festival discounts, one-time sale offers,etc. Since then, there are many sites that have their own price lists based on their own discountschemes. A layman would have to work his way through various other e-commerce websites toget the best product at the right price.
The main problems are as follows:
1. Consumers are confused by the many e-commerce websites selling the same product.
2. Consumers want specifications of the product on touch or scan.
3. Retailers have to employ individuals with knowledge of the product specifications.
4. The brand/company wants useful interaction with the customer.
5. Scam/fake products on e-commerce require an authentication mechanism.


SOLUTION

“FreeCom” acts as a tool to assist consumers in making informed decisions before purchasing aproduct by providing a list of prices offered by different retailers/supermarkets. Users will use thiswebsite as their reference to check on the price of electronic products sold and see if there is anypromotion going on. It is also able to help sellers promote new products by sending emails to thesubscribers about them. Users will use this website to check out the difference between theelectronic devices that seem to have almost the same price but may have different specifications.Instead of taking hours and energy to go to each shop just to check on the price, “FreeCom” offersa better solution by getting all the prices in one place. Users just need to go online and choosewhich product they want to know about, and the list of retailers and the price offered will be shown. Users can check it from anywhere, no matter if they are at home or at work, or even on the trainwhile going back from work. “FreeCom” is accessible anytime as long as there is an internet
connection. Users can also check the authenticity of the product that they bought using the QR code scanner on our site.Shoppers usually consult about four websites (on average) for price and feature information.Among all consumers who are purchasing products offline, roughly two-thirds begin their searchesonline, using a combination of search websites and the retailer’s own website.We are proposing to implement a QR-based comparison in which consumers will scan the QRcode available with the product and get the comparison between the two. Users can use our webapplication to scan the creative arts, images, and logos to check whether they get a discount oroffer. Product Analysis will help consumers analyse the trending products on Amazon.The development of “FreeCom” will help consumers increase their price consciousness, help themmake informed decisions to save money and help the sellers advertise for free.