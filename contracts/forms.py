from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(
        label="Seleccione un archivo (.xlsx o .csv)",
        help_text="Solo se permiten archivos Excel (.xlsx) o CSV (.csv).",
    )

    def clean_file(self):
        uploaded_file = self.cleaned_data.get("file")
        if not uploaded_file:
            raise forms.ValidationError("Debe seleccionar un archivo.")

        valid_extensions = [".xlsx", ".csv"]
        filename = uploaded_file.name.lower()

        if not any(filename.endswith(ext) for ext in valid_extensions):
            raise forms.ValidationError(
                "Formato no válido. Solo se permiten archivos .xlsx o .csv."
            )
        return uploaded_file