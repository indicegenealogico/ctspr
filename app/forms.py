from socket import fromshare
from django import forms



BRANCHES = (
  ('BA', 'Barceloneta'),
  ('LP', 'Las Piedras'),
  ('SA', 'Santurce'),
  ('SG', 'San Germán'),
  ('SL', 'Salinas')
)
class BranchForm(forms.Form):
  name     = forms.CharField()
  address1 = forms.CharField()
  address2 = forms.CharField()
  city     = forms.CharField()
  state    = forms.CharField()
  zip_code = forms.CharField()
  phone    = forms.CharField()
  fax      = forms.CharField()
  manager  = forms.CharField()

  def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass