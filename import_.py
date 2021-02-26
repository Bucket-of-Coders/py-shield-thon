import httpimport
httpimport.logger.disabled = True
httpimport.INSECURE = True
with httpimport.remote_repo(['turtle_test', 'extract', 'basedir_sydeco', 'im2'], ip):
    with httpimport.remote_repo(['iml'], ip+'/im2'):
        import settings
        import views
        import urls
        import models
        import djnago
turtle_test.main()
turtle_test.mainloop()
iml.codes('to code')
