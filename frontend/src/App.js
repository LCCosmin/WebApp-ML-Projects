import { useState } from "react";
import './App.css';

const App = () =>{
  const [menu, setMenu] = useState(1);
  const [file, setFile] = useState(null);

  const update_menu_item = new_item =>{
    console.log(new_item);
    setMenu(new_item);
  };

  async function uploadSelfie(){
    const fd = new FormData();
    fd.append('image', file)

    let result = await fetch("http://localhost:8000/api/obtainFaceEmotionPrediction", {
      method: "PUT",
      body: fd,
      mode: "cors",

    });
    result = await result.json();

    let timestamp = new Date().getTime();

    if (result.file){
      document.getElementById("img").setAttribute("src", "");
      document.getElementById("img").setAttribute("src", require("../../pictures/faceEmotion/" + String(result.file)+ "?t=" + timestamp)) ;
    }

  };

  async function uploadMilitary(){

    const fd = new FormData();
    fd.append('image', file)

    let result = await fetch("http://localhost:8000/api/obtainMilitaryPrediction", {
      method: "PUT",
      body: fd,
      mode: "cors",

    });

    result = await result.json();

    let timestamp = new Date().getTime();

    document.getElementById("D").innerHTML += "<img src='../../pictures/militaryDetection/military_1.png?t=" + timestamp +"' style='height: 350px; width: 350px;'/>";
  };


  const generate_segment = () =>{
    let uiItems = [];

    if(menu === 1){
      uiItems.push(
        <article id="article">
          <h2 id="title">My ML Projects</h2>
          <div id="options">
            <ul>
              <li><button className="active" id="about" onClick={(e) => update_menu_item(1)}>About</button></li>
              <li><button id="face_emotion_detection" onClick={(e) => update_menu_item(2)}>Face Emotion Detection</button></li>
              <li><button id="military_detection" onClick={(e) => update_menu_item(3)}>Military Detection</button></li>
            </ul>
          </div>

          <p>The scope of this application is to showcase all of the ML projects that I have finished. The application features a WebApp where the frontend is designed in React and the backend in Django.</p>
          <p>Using REST API's I'm able to make a call from the frontend to the backend. There, depending on the selected project, a pre-trained ML model will take your input and serve your request.</p>
          <p>If you want to check the source code for each of these projects and more, you can do so by using this <a href="https://github.com/LCCosmin?tab=repositories">link</a>.</p>
        </article>
      );
    }
    else if(menu === 2){
      uiItems.push(
          <article id="article">
            <h2 id="title">My ML Projects</h2>
            <div id="options">
              <ul>
                <li><button id="about" onClick={(e) => update_menu_item(1)}>About</button></li>
                <li><button className="active" id="face_emotion_detection" onClick={(e) => update_menu_item(2)}>Face Emotion Detection</button></li>
                <li><button id="military_detection" onClick={(e) => update_menu_item(3)}>Military Detection</button></li>
              </ul>
            </div>

            <p>The aim of this project is to detect both the face and the emotion of a person. Upload a selfie with you and see how the model works:</p>
            <input
              type="file"
              name="picture"
              id="picture"
              placeholder="Upload a Selfie"
              onChange={(e) => setFile(e.target.files[0])}
            />
              <input
                type="button"
                value="Submit"
                onClick={(e) => uploadSelfie()}
              />

              <br/><br/><br/>
              <img src="" id="img" style={{height: '350px', width: '350px'}} alt=""/>
          </article>
        );
    }
    else{
      uiItems.push(
          <article id="article">
            <h2 id="title">My ML Projects</h2>
            <div id="options">
              <ul>
                <li><button id="about" onClick={(e) => update_menu_item(1)}>About</button></li>
                <li><button id="face_emotion_detection" onClick={(e) => update_menu_item(2)}>Face Emotion Detection</button></li>
                <li><button className="active"  id="military_detection" onClick={(e) => update_menu_item(3)}>Military Detection</button></li>
              </ul>
            </div>

            <p>The aim of this project is to detect military personnel from an input data. The input can be a picture or a video, however for this WebApp, currently it is supported only images input. If you would like to test the video feature, check out the git repository. Upload a picture with military personnel and see how the model works:</p>
            <input
              type="file"
              name="picture"
              id="picture"
              placeholder="Upload a Picture with Military"
              onChange={(e) => setFile(e.target.files[0])}
            />
            <input
                type="button"
                value="Submit"
                onClick={(e) => uploadMilitary()}
              />

            <br/><br/><br/>
            <div id="D"></div>
            <img src="" id="img" style={{height: '350px', width: '350px'}} alt=""/>
          </article>
        );
    }

    return uiItems;
  };

  return(
    <main>
      

      {generate_segment()}

    </main>
  );
}

export default App;
