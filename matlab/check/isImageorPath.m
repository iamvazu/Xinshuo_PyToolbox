% Author: Xinshuo Weng
% email: xinshuo.weng@gmail.com

% this function gets a file id while saving txt given a path
function img = isImageorPath(img)
    if ischar(img)
        img = imread(img);
    else
        assert(isimage(img), ...
            'The input image doesn''t have a good dimension.');
    	img = img;
    end
end