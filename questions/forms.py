from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['topic', 'marks', 'subject', 'asked', 'content']

    def clean(self):
        data = self.cleaned_data
        topic = data.get("topic")
        qs = Question.objects.filter(topic__icontains=topic)
        if qs.exists():
            self.add_error("topic", f"{topic} is already in use")
        content = data.get("content")
        if "sai" in content or "sai" in topic:
            self.add_error("topic", "we don't let uruks in our club, this is elvish businnes you maggot")
        return data