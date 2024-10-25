from django import forms

class ProposalUploadForm(forms.Form):
    title = forms.CharField(max_length=255)
    proposal_file = forms.FileField()
