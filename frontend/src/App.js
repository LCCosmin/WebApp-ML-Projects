import { Component } from "react";
import axios from "axios";
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      menu: 1,
      file: null
    };
  }

  fileSelect = event =>{
    this.setState({file: event.target[0]});
  }

  update_menu_item(new_item){
    this.setState({menu: new_item});
  }

  uploadSelfie(){
    axios
    .put("http://127.0.0.1:8000/api/obtainFaceEmotionPrediction", this.state.file)
    .then((response) => {
      if (response.data){
        document.getElementById("article").innerHTML +=
              "<img src=" + response.data.file + "/>";
      }
      else{
        document.getElementById("article").innerHTML +=
              "<h2>No faces were detected :(</h2>"
      }
    })
    .catch((err) => console.log(err));
  }

  uploadMilitary(){
    axios
    .put("http://127.0.0.1:8000/api/obtainMilitaryPrediction", this.state.file)
    .then((response) => {
      if (response.data){
        let non_military = response.data.file[0];
        let military = response.data.file[1];

        document.getElementById("article").innerHTML +=
              "<div className='scroll-container'><div className='gridscroll'><h4>Non-Military</h4></div></div>"

        non_military.forEach(element => {
          document.getElementById("gridscroll").innerHTML +=
              "<img src=" + element + "/>";
        });

        document.getElementById("gridscroll").innerHTML +=
              "<h4>Military</h4>";

        military.forEach(element =>{
          document.getElementById("gridscroll").innerHTML +=
              "<img src=" + element + "/>";
        })
      }
      else{
        document.getElementById("article").innerHTML +=
              "<h2>No persons were detected :(</h2>"
      }
    })
    .catch((err) => console.log(err));
  }

  

  generate_segment(){
    let uiItems = [];

    if(this.state.menu === 1){
      uiItems.push(
        <article id="article">
          <h2 id="title">My ML Projects</h2>
          <div id="options">
            <ul>
              <li><button className="active" id="about" onClick={(e) => this.update_menu_item(1)}>About</button></li>
              <li><button id="face_emotion_detection" onClick={(e) => this.update_menu_item(2)}>Face Emotion Detection</button></li>
              <li><button id="military_detection" onClick={(e) => this.update_menu_item(3)}>Military Detection</button></li>
            </ul>
          </div>

          <p>The scope of this application is to showcase all of the ML projects that I have finished. The application features a WebApp where the frontend is designed in React and the backend in Django.</p>
          <p>Using REST API's I'm able to make a call from the frontend to the backend. There, depending on the selected project, a pre-trained ML model will take your input and serve your request.</p>
          <p>If you want to check the source code for each of these projects and more, you can do so by using this <a href="https://github.com/LCCosmin?tab=repositories">link</a>.</p>
        </article>
      )
    }
    else if(this.state.menu === 2){
      uiItems.push(
          <article id="article">
            <h2 id="title">My ML Projects</h2>
            <div id="options">
              <ul>
                <li><button id="about" onClick={(e) => this.update_menu_item(1)}>About</button></li>
                <li><button className="active" id="face_emotion_detection" onClick={(e) => this.update_menu_item(2)}>Face Emotion Detection</button></li>
                <li><button id="military_detection" onClick={(e) => this.update_menu_item(3)}>Military Detection</button></li>
              </ul>
            </div>

            <p>The aim of this project is to detect both the face and the emotion of a person. Upload a selfie with you and see how the model works:</p>
            <input
              type="file"
              name="picture"
              id="picture"
              placeholder="Upload a Selfie"
              onChange={(e) => this.fileSelect}
            />
            <input
              type="button"
              value="Submit"
              onClick={(e) => this.uploadSelfie()}
            />
          </article>
        )
    }
    else{
      uiItems.push(
          <article id="article">
            <h2 id="title">My ML Projects</h2>
            <div id="options">
              <ul>
                <li><button id="about" onClick={(e) => this.update_menu_item(1)}>About</button></li>
                <li><button id="face_emotion_detection" onClick={(e) => this.update_menu_item(2)}>Face Emotion Detection</button></li>
                <li><button className="active"  id="military_detection" onClick={(e) => this.update_menu_item(3)}>Military Detection</button></li>
              </ul>
            </div>

            <p>The aim of this project is to detect military personnel from an input data. The input can be a picture or a video, however for this WebApp, currently it is supported only images input. If you would like to test the video feature, check out the git repository. Upload a picture with military personnel and see how the model works:</p>
            <input
              type="file"
              name="picture"
              id="picture"
              placeholder="Upload a Picture with Military"
              onChange={(e) => this.fileSelect}
            />
            <input
              type="button"
              value="submit"
              onClick={(e) => this.uploadMilitary()}
            />
          </article>
        )
    }

    return uiItems;
  }

  render(){
    return(
      <main>
        

        {this.generate_segment()}
      </main>
    );
  }
}

export default App;
