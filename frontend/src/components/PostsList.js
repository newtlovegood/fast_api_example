import  React, { Component } from  'react';
import  DiaryService  from  '../DiaryService';

const  diaryService  =  new  DiaryService();

class  PostsList  extends  Component {

	constructor(props) {
		super(props);
		this.state  = {
			posts: [],
		};
	}

	componentDidMount() {
		diaryService.getPosts().then(response => {
			this.setState({
			  posts: response
			});
		  });
		
	}

	render() {
		let href;
		console.log('render');
		return (
			<div className='posts'>
				{this.state.posts.map((post) => (
					href = `posts/${post.id}`,
					<div key={post.id} id={post.id} className='post'>
						<p><a href={href}>{post.title}</a></p>
					</div>
				))}
			</div>
		)
	}
}
export  default  PostsList;
