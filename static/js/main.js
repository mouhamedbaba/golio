let register = new Register("Text2")
register.resgister_site()
setTimeout(() => {
    register.register_guest()
}, 5000);
setTimeout(() => {
    register.register_page()
}, 10000)