require 'test_helper'

class HelpersControllerTest < ActionDispatch::IntegrationTest
  setup do
    @helper = helpers(:one)
  end

  test "should get index" do
    get helpers_url
    assert_response :success
  end

  test "should get new" do
    get new_helper_url
    assert_response :success
  end

  test "should create helper" do
    assert_difference('Helper.count') do
      post helpers_url, params: { helper: { helper_score: @helper.helper_score } }
    end

    assert_redirected_to helper_url(Helper.last)
  end

  test "should show helper" do
    get helper_url(@helper)
    assert_response :success
  end

  test "should get edit" do
    get edit_helper_url(@helper)
    assert_response :success
  end

  test "should update helper" do
    patch helper_url(@helper), params: { helper: { helper_score: @helper.helper_score } }
    assert_redirected_to helper_url(@helper)
  end

  test "should destroy helper" do
    assert_difference('Helper.count', -1) do
      delete helper_url(@helper)
    end

    assert_redirected_to helpers_url
  end
end
