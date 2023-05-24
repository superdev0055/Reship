from django.http import HttpResponse
from django.template import loader
def index_animation(request):
  template = loader.get_template('index-animation.html')
  return HttpResponse(template.render())
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def about_us(request):
  template = loader.get_template('about-us.html')
  return HttpResponse(template.render())
def blog_left(request):
  template = loader.get_template('blog-left.html')
  return HttpResponse(template.render())
def blog(request):
  template = loader.get_template('blog.html')
  return HttpResponse(template.render())
def coming_soon(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def contact_us_2(request):
  template = loader.get_template('contact-us-2.html')
  return HttpResponse(template.render())
def contact_us(request):
  template = loader.get_template('contact-us.html')
  return HttpResponse(template.render())
def get_quote(request):
  template = loader.get_template('get-quote.html')
  return HttpResponse(template.render())
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def index_2(request):
  template = loader.get_template('index-2.html')
  return HttpResponse(template.render())
def index_3(request):
  template = loader.get_template('index-3.html')
  return HttpResponse(template.render())

def pricing_plans(request):
  template = loader.get_template('pricing-plans.html')
  return HttpResponse(template.render())
def single_blog(request):
  template = loader.get_template('single-blog.html')
  return HttpResponse(template.render())
def tracking(request):
  template = loader.get_template('tracking.html')
  return HttpResponse(template.render())
