# coding: utf-8

class PostsController < ApplicationController

  def index
    # instance var is accessible from view
    @posts = Post.all(:order => "created_at DESC")
  end

  def show
    @post = Post.find(params[:id])
  end

  def new
    @post = Post.new
  end

  def create
    @post = Post.new(params[:post])
    if @post.save
      redirect_to posts_path, notice: '作成されました!'
    else
      render action: 'new'
    end
  end

end
