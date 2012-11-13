class PostsController < ApplicationController

  def index
    @posts = Post.all  # instance var is accessible from view
  end

  def show
    @post = Post.find(params[:id])
  end

end
