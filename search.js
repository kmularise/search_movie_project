const SearchForm = document.getElementById("search-form");
const server =`http://localhost:8000/`;
const naver_api = server + 'naver/api/';

document.getElementById("search-form").onsubmit = function() {
    var key = document.getElementById("search-form")[0].value;
    console.log('key is : ' + key);

    fetch(naver_api + key).then(response => response.json()).then(data => {
        console.log(data);
        const title = document.querySelector("#movie p span:first-child");
        const director = document.querySelector("#movie p span:last-child");
        const image = document.querySelector("#image span:first-child");

        if (data.items == 0) {
            title.innerHTML = "제목 정보 없음";
            director.innerHTML = "감독 정보 없음";
            image.innerHTML= "<img src='no_image' alt='이미지 없음'/>";
        }
        else {
            title.innerHTML = data.items[0].title;
            director.innerHTML = data.items[0].director;
            image.innerHTML= "<img src='"+data.items[0].image+"' alt='이미지 없음'/>";
        }

    });
    return false;
}

