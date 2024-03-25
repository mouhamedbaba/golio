const resgister_site = () =>{
    let Name = "Golio"
    // let Url = window.location.href
    let page_title = document.title
    let data = {
        Name,
        Url,
        Autre : {
            page_title, 
            description : "Golio est un site de développement web",
        }
    }
    fetch('http://127.0.0.1:5000/register_site', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(
        response => console.log(response)
    )
    .catch(error => console.log(error))
} 

const register_user = () => {
    let list_page_ids = localStorage.getItem('list_page_ids')
    console.log(list_page_ids);
    if (list_page_ids == null) {
        localStorage.setItem("list_page_ids", [])
    }
    list_page_ids = localStorage.getItem('list_page_ids')
    // Construct the query string with parameters
    const queryParams = new URLSearchParams({
        path: window.location.pathname,
        url: window.location.href,
        page_title: document.title,
        list_page_id : list_page_ids
    });

    // Construct the full URL with the query parameters
    const url = "/register_user?" + queryParams.toString();

    // Fetch the URL with a GET request
    fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log("data");
        console.log(data);
        if (data.page_id != null ) {
        let new_list =  list_page_ids.split(',')
        new_list.push(data.page_id)
        localStorage.setItem("list_page_ids", new_list)
        
        }
    })
    .catch(error => console.log(error));
}


// resgister_site()
// register_user()

