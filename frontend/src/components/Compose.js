// textarea that expands with the content growth
// for now just text as markdown (e.g. **example**)

import { Component } from "react";
import DiaryService from '../DiaryService';
import { fetchToken } from "./Login/login";

const diaryService = new DiaryService();

class MyEditor extends Component {
    constructor(props) {
        super(props);
        this.state = {
            title: '',
            content: ''
        }
    }

    render() {
        return (
            <div className="editor-container">
                <div><input type='text' placeholder="Title" onChange={e => this.setState({title: e.target.value})}></input></div>
                <div><textarea placeholder="Write your thoughts" onChange={e => this.setState({content: e.target.value})}></textarea></div>
                <button onClick={() => {
                        diaryService.createPost(fetchToken(), {'title': this.state.title, 'content': this.state.content})
                    }}
                    >Save a record</button>
            </div>
        )
    }
}

export default MyEditor;