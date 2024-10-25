from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Proposal
from .serializers import ProposalSerializer
from .forms import ProposalUploadForm  # New form for handling file uploads
from .utils.nlp_processing import parse_proposal_text  # NLP processing function

# Existing API view
class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

# New frontend view for file upload and evaluation
def upload_proposal_view(request):
    if request.method == 'POST':
        form = ProposalUploadForm(request.POST, request.FILES)
        if form.is_valid():
            proposal_file = request.FILES['proposal_file']
            # Create a new Proposal instance
            proposal = Proposal.objects.create(title=form.cleaned_data['title'], document=proposal_file)
            # Process the uploaded file's content
            evaluation_result = parse_proposal_text(proposal.document.read().decode('utf-8'))
            # Pass the results to a template
            return render(request, 'proposal_evaluation/result.html', {'evaluation_result': evaluation_result})
    else:
        form = ProposalUploadForm()
    return render(request, 'proposal_evaluation/upload.html', {'form': form})
