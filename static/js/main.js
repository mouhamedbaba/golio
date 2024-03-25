let register = new Register("Golio")
register.resgister_site()
setTimeout(() => {
    register.register_guest()
}, 5000);
setTimeout(() => {
    register.register_page()
}, 10000)