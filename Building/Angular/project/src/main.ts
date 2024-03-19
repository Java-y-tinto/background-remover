import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { FormularioComponent } from './app/formulario/formulario.component';

bootstrapApplication(FormularioComponent, appConfig)
  .catch((err) => console.error(err));
