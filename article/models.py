#coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
from collections import OrderedDict
from django.utils.encoding import force_bytes

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50,blank=True)
    website=models.URLField(blank=True)
    def __str__(self):
        return force_bytes(self.name)
    # def __str__(self):
    #     return self.name.encode('utf-8')

class TagManager(models.Manager):
    def get_Tag_list(self):
        tags=Tag.objects.all()
        tag_list=[]
        for i in range(len(tags)):
            tag_list.append([])
        for i in range(len(tags)):
            temp=Tag.objects.get(name=tags[i])
            posts=temp.article_set.all()
            tag_list[i].append(tags[i].name)
            tag_list[i].append(len(posts))
        return tag_list

class Tag(models.Model):
    name=models.CharField(max_length=20,blank=True)
    create_time=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    tag_list=TagManager()

    def get_absolute_url(self):
        return reverse('tagDetail',args={'tag':self.name})

    def __str__(self):
        return force_bytes(self.name)
    # def __str__(self):
    #     return self.name.encode('utf-8')

class ClassManager(models.Manager):
    def get_Class_list(self):
        classf=Classification.objects.all()
        class_list=[]
        for i in range(len(classf)):
            class_list.append([])
        for i in range(len(classf)):
            temp=Classification.objects.get(name=classf[i])
            posts=temp.article_set.all()
            class_list[i].append(classf[i])
            class_list[i].append(len(posts))
        return class_list

class Classification(models.Model):
    name=models.CharField(max_length=50)
    objects=models.Manager()
    class_list=ClassManager()

    def __str__(self):
        return force_bytes(self.name)
    # def __unicode__(self):
    #     return self.name.encode('utf-8')

class ArticleManager(models.Model):
    def get_Article_onDate(self):
        post_date=Article.objects.datetimes('publish_time','month')
        date_list=[]
        for i in range(len(post_date)):
            date_list.append([])
        for i in range(len(post_date)):
            curyear=post_date[i].year
            curmonth=post_date[i].month
            tempArticle=Article.objects.filter(publish_time__year=curyear).filter(publish_time__month=curmonth)
            tempNum=len(tempArticle)
            date_list[i].append(post_date[i])
            date_list[i].append(tempNum)
        return date_list

    def get_Article_OnArchive(self):
        post_date=Article.objects.datetimes('publish_time','month')
        post_date_article=[]

        for i in range(len(post_date)):
            post_date_article.append([])

        for i in range(len(post_date)):
            curyear=post_date[i].year
            curmonth=post_date[i].month
            tempArticle=Article.objects.filter(publish_time__year=curyear).filter(publish_time__month=curmonth)
            post_date_article[i]=tempArticle

        dicts=OrderedDict()
        for i in range(len(post_date)):
            dicts.setdefault(post_date[i],post_date_article[i])
        return dicts


class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author)
    tags=models.ManyToManyField(Tag,blank=True)
    classification=models.ForeignKey(Classification)
    content=models.TextField(blank=True,null=True)
    publish_time=models.DateTimeField(auto_now_add=True)
    count=models.IntegerField(default=0)

    objects=models.Manager()
    date_list=ArticleManager()

    # def get_absolute_url(self):
    #     return reverse('detail',args=(self.publish_time,self.publish_time.strftime('%m'),
    #                self.publish_time.strftime('%d'),self.id),)

    @models.permalink
    def get_absolute_url(self):
      return ('detail', (), {
       'year': self.publish_time.year,
       'month': self.publish_time.strftime('%m'),
       'day': self.publish_time.strftime('%d'),
       'id': self.id})

    def get_tags(self):
        tag=self.tags.all()
        return tag

    def get_before_article(self):
        temp=Article.objects.order_by('id')
        cur=Article.objects.get(id=self.id)
        count=0
        for i in temp:
            if i.id==cur.id:
                index=count
                break
            else:
                count=count+1
        if index!=0:
            return temp[index-1]

    def get_after_article(self):
        temp=Article.objects.order_by('id')
        max=len(temp)-1
        cur=Article.objects.get(id=self.id)
        count=0
        for i in temp:
            if i.id==cur.id:
                index=count
                break
            else:
                count=count+1
        if index!=max:
            return temp[index+1]

    def __str__(self):
        return force_bytes(self.title)

    # def __str__(self):
    #     return self.title.encode('utf-8')

    class Meta:
        ordering=['-publish_time']

